namespace Csharp
{
    public static class Day1
    {
        const string fileName = "..\\day1\\input.txt";

        public static void Run()
        {
            var numbers = File.ReadAllLines(fileName).ToList().Where(l => l != string.Empty).Select(i => int.Parse(i)).ToList();
            Console.WriteLine("Day 1:");
            part1(numbers);
            part2(numbers);
        }

        static void part1(List<int> numbers)
        {
            var sum = 0;

            for (var i = 0; i < numbers.Count - 1; i++)
            {
                if (numbers[i] < numbers[i + 1])
                {
                    sum++;
                }
            }

            Console.WriteLine(sum);
        }

        static void part2(List<int> numbers)
        {
            var sum = 0;

            for (var i = 0; i < numbers.Count - 3; i++)
            {
                var measure1 = numbers[i] + numbers[i + 1] + numbers[i + 2];
                var measure2 = numbers[i + 1] + numbers[i + 2] + numbers[i + 3];

                if (measure1 < measure2)
                {
                    sum++;
                }
            }

            Console.WriteLine(sum);
        }
    }
}