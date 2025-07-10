using System.Collections.Generic;
using CSnakes.Runtime.Python;

Console.WriteLine("=== CSnakes Program 1 ===");

var builder = Host.CreateDefaultBuilder(args)
    .ConfigureServices((context, services) =>
    {
        var home = Path.Join(Environment.CurrentDirectory, ".");
        var pythonScriptsPath = Path.Join(Environment.CurrentDirectory, "python-scripts");
        services
            .WithPython()
            .WithHome(home)
            .FromRedistributable(); // Use FromRedistributable instead of FromAssembly
    });

var app = builder.Build();
var env = app.Services.GetRequiredService<IPythonEnvironment>();

// Add the python-scripts directory to sys.path
var pythonScriptsPath = Path.Join(Environment.CurrentDirectory, "python-scripts");
env.Execute($"import sys\nsys.path.insert(0, '{pythonScriptsPath.Replace("\\", "/")}')", new Dictionary<string, PyObject>(), new Dictionary<string, PyObject>());

// Get the generated module
var module = env.ScriptDemo();

Console.WriteLine("1. Calling simple greet function:");
var greetResult = module.Greet("World");
Console.WriteLine($"   Result: {greetResult}");

Console.WriteLine("\n2. Calling create_greeter function:");
var greeterResult = module.CreateGreeter("Hi");
Console.WriteLine($"   Result: {greeterResult}");

Console.WriteLine("\n3. Calling greet_with_custom_message function:");
var customGreetResult = module.GreetWithCustomMessage("Alice", "Good morning");
Console.WriteLine($"   Result: {customGreetResult}");

Console.WriteLine("\n3. Calling process_multiple_greetings function:");
var returnGreentings = module.ProcessMultipleGreetings(new[] { "Alice", "Bob", "Charlie" });
foreach (var greeting in returnGreentings)
{
    Console.WriteLine($"   Greeting: {greeting}");
}

Console.WriteLine("\n=== CSnakes is working successfully! ===");