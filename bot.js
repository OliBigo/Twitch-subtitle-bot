const tmi = require("tmi.js");
const fs = require("fs");
const request = require("snekfetch");
require("dotenv").config();

// Define configuration options
const opts = {
  identity: {
    username: process.env.USERNAME,
    password: process.env.PASSWORD,
  },
  channels: ["zoil"],
};

// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on("connected", onConnectedHandler);

//client.on("hosting", onHostingHandler);

// Connect to Twitch:
client.connect();

// Called every time the bot connects to Twitch chat
function onConnectedHandler(addr, port) {
  console.log(`* Connected to ${addr}:${port}`);
}

const api = `https://api.twitch.tv/helix/streams?user_login=${opts.channels[0].substring(
  1
)}`;

var isLive = false;

setInterval(() => {
  request
    .get(api)
    .set("Authorization", process.env.AUTHORIZATION)
    .set("Client-ID", process.env.CLIENT_ID)
    .then((response) => {
      if (response.body.data.length == 0) {
        if (isLive) offlineHandler(opts.channels[0].substring(1));
        isLive = false;
      } else {
        if (!isLive) liveHandler(opts.channels[0].substring(1));
        isLive = true;
      }
    });
}, 300000);

function liveHandler(channel) {
  console.log("Went live: now watching file");
  fs.writeFileSync("status.txt", "true", { encoding: "utf-8" });
  fs.watchFile(channel + ".txt", () => {
    let text = getFileText(channel);
    if (text) {
      let splitText = text.replaceAll("!", ".").replaceAll("?", ".").split(".");
      splitText.pop();
      if (splitText.length > 0) {
        let message = chooseMessage(splitText);
        if (message) {
          if (message.includes("fifteen") || message.includes("15"))
            sendSwagMessage(message, channel);
          else sendNormalMessage(message, channel);
        }
      }
    }
  });
}

function offlineHandler(channel) {
  console.log("Went offline: stopped watching file");
  fs.writeFileSync("status.txt", "false", { encoding: "utf-8" });
  fs.unwatchFile(channel + ".txt");
}

function getFileText(channel) {
  let data = fs.readFileSync(channel + ".txt", { encoding: "utf8" });
  return data;
}

function chooseMessage(text) {
  let lastWords = text.pop();
  if (lastWords && lastWords.length > 100) {
    split = lastWords.split(" ");
    split.length = 15;
    return split.join(" ");
  } else if (lastWords.length < 50) {
    let message = lastWords;
    while (message.length < 50 && text.length != 0) {
      message = text.pop() + ". " + message;
    }

    if (message.length > 100) {
      let splitMessage = message.split(".");
      splitMessage.shift();
      let newMessage = splitMessage.join(". ");
      if (newMessage.length > 50) return newMessage;
    } else return message;
  } else return lastWords;
}

function eraseFile(file) {
  try {
    fs.writeFileSync(file, "");
  } catch (error) {
    console.log("Was saving");
  }
}

function sendNormalMessage(text, channel) {
  console.log("Sending normal message: Barry63 " + text);
  client.say(channel, "Barry63 " + text);
  eraseFile(channel + ".txt");
}

function sendSwagMessage(text, channel) {
  console.log("Sending swag message: Swag " + text);
  client.say(channel, "Swag " + text);
  eraseFile(channel + ".txt");
}
