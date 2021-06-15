using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var t1 = Dance();
        var t2 = LearnAndSing();

        var tasks = new List<Task> { t1, t2 };
        while (tasks.Count > 0)
        {
            Task finishedTask = await Task.WhenAny(tasks);
            tasks.Remove(finishedTask);
        }
    }

    public static async Task Dance()
    {
        for (int i = 0; i < 10; i++)
        {
            await Task.Delay(100);
            Console.WriteLine($"{i}");
        }
    }

    public static async Task<string> LearnSong()
    {
        await Task.Delay(600);
        return "this is the song";
    }

    public static void SingSong(string song)
    {
        Console.WriteLine(song);
    }


    public static async Task LearnAndSing()
    {
        string song = await LearnSong();
        SingSong(song);
    }
}
