function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function learnSong() {
  await sleep(600);
  return 'this is the song';
}

async function singSong(song) {
  console.log(song);
}

async function learnAndSing() {
  const song = await learnSong();
  await singSong(song);
}

async function dance() {
  for (let i = 0; i <= 10; i += 1) {
    await sleep(100);
    console.log(i);
  }

  return 'done dancing';
}

async function main() {
// it takes 600ms to learn the song, then it will be sung.
  learnAndSing();

  // a dance move takes 100ms before it's visible.
  dance().then((value) => {
    console.log(value);
  });

  // let's go!
  console.log('waiting to learn the song, sing it and daaance!');
}

main();
