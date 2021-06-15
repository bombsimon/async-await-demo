fn main() {
    futures::executor::block_on(async_main());
}

async fn async_main() {
    let f1 = learn_and_sing();
    let f2 = dance();

    // `join!` is like `.await` but can wait for multiple futures concurrently.
    // If we're temporarily blocked in the `learn_and_sing` future, the `dance`
    // future will take over the current thread. If `dance` becomes blocked,
    // `learn_and_sing` can take back over. If both futures are blocked, then
    // `async_main` is blocked and will yield to the executor.
    futures::join!(f1, f2);
}

async fn learn_and_sing() {
    // Wait until the song has been learned before singing it.
    // We use `.await` here rather than `block_on` to prevent blocking the
    // thread, which makes it possible to `dance` at the same time.
    let song = learn_song().await;
    sing_song(song).await;
}

async fn learn_song() -> String {
    async_std::task::sleep(std::time::Duration::from_millis(600)).await;
    String::from("this is the song")
}

async fn sing_song(song: String) {
    println!("{}", song)
}

async fn dance() {
    for i in 0..10 {
        async_std::task::sleep(std::time::Duration::from_millis(100)).await;
        println!("{}", i)
    }
}
