namespace Csharp
{
    public static class Day3
    {
        const string fileName = "..\\day3\\exampleinput.txt";

        public static void Run()
        {
            IEnumerable<Command> commands = File
                .ReadAllLines(fileName)
                .Where(l => l != string.Empty)
                .ToList();

            Console.WriteLine("Day 3:");
            part1(commands);
            part2(commands);
        }

        static void part1(IEnumerable<Command> commands)
        {
            
        }

        static void part2(IEnumerable<Command> commands)
        {
            
        }
    }

}