const redis = require('redis');
const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
    if (message === 'KILL_SERVER')  {
      client.unsubscribe(channel);
      client.quit();
    }
  }
});

client.subscribe('holberton school channel');
