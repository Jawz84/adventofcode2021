namespace Csharp
{
    public static class Day2
    {
        const string fileName = "..\\day2\\exampleinput.txt";

        public static void Run()
        {
            IEnumerable<Command> commands = File
                .ReadAllLines(fileName)
                .Where(l => l != string.Empty)
                .Select(l => new Command(l));

            Console.WriteLine("Day 2:");
            part1(commands);
            part2(commands);
        }

        static void part1(IEnumerable<Command> commands)
        {
            var distance = 0;
            var depth = 0;

            foreach (var command in commands)
            {
                switch (command.type)
                {
                    case CommandType.forward:
                        distance += command.amount;
                        break;
                    case CommandType.up:
                        depth -= command.amount;
                        break;
                    case CommandType.down:
                        depth += command.amount;
                        break;
                }
            }

            Console.WriteLine(distance * depth);
        }

        static void part2(IEnumerable<Command> commands)
        {
            var distance = 0;
            var depth = 0;
            var aim = 0;

            foreach (var command in commands)
            {
                switch (command.type)
                {
                    case CommandType.forward:
                        distance += command.amount;
                        depth += aim * command.amount;
                        break;
                    case CommandType.up:
                        aim -= command.amount;
                        break;
                    case CommandType.down:
                        aim += command.amount;
                        break;
                }
            }

            Console.WriteLine(distance * depth);
        }
    }

    class Command
    {
        public CommandType type;
        public int amount;

        public Command(string rawCommand)
        {
            var parts = rawCommand.Split(' ');
            this.type = Enum.Parse<CommandType>(parts[0]);
            this.amount = int.Parse(parts[1]);
        }
    }

    public enum CommandType
    {
        forward,
        up,
        down
    }
}