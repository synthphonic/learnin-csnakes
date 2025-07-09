# Getting Started with CSnakes and .NET Console App

## Step 1: Set Up Your .NET Console Application

1. **Create a New .NET Console Project:**
   - Open your terminal and navigate to the directory where you want to create your project.
   - Run the following command to create a new .NET console application:
     ```bash
     dotnet new console -n MyCSnakesApp
     ```
   - Navigate into the project directory:
     ```bash
     cd MyCSnakesApp
     ```

2. **Add the CSnakes NuGet Package:**
   - Install the `CSnakes.Runtime` package to your project by running:
     ```bash
     dotnet add package CSnakes.Runtime
     ```

## Step 2: Set Up Python Environment

1. **Install Python:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Python Script:**
   - Inside your project directory, create a Python file, e.g., `script.py`, with the following content:
     ```python
      def greet(name: str) -> str:
          return f"Hello, {name}!"

      def create_greeter(greeting: str) -> str:
          """Creates a greeting message with a custom greeting."""
          return f"{greeting}, World!"

      def greet_with_custom_message(name: str, greeting: str) -> str:
          """Greets someone with a custom greeting message."""
          return f"{greeting}, {name}!"

      class Greeter:
          def __init__(self, greeting: str):
              self.greeting = greeting

          def greet_in_class(self, name: str) -> str:
              return f"{self.greeting}, {name}!"    
     ```

3. **Mark Python File for Source Generation:**
   - Open your `.csproj` file and add the Python file as an additional file:
     ```xml
      <ItemGroup>
        <AdditionalFiles Include="ScriptDemo.py">
          <CopyToOutputDirectory>Always</CopyToOutputDirectory>
        </AdditionalFiles>
      </ItemGroup>
     ```

## Step 3: Configure Your .NET Application

1. **Modify `Program.cs`:**
   - Open `Program.cs` and set up the Python environment and call the Python functions:
   ```csharp
    Console.WriteLine("=== CSnakes Program 1 ===");

    var builder = Host.CreateDefaultBuilder(args)
        .ConfigureServices((context, services) =>
        {
            var home = Path.Join(Environment.CurrentDirectory, ".");
            services
                .WithPython()
                .WithHome(home)
                .FromRedistributable(); // Use FromRedistributable instead of FromAssembly
        });

    var app = builder.Build();
    var env = app.Services.GetRequiredService<IPythonEnvironment>();

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

    Console.WriteLine("\n=== CSnakes is working successfully! ===");
   ```

## Step 4: Build and Run Your Application

1. **Build the Project:**
   - Run the following command to build your project:
     ```bash
     dotnet build
     ```

2. **Run the Application:**
   - Execute your application to see the output:
     ```bash
     dotnet run
     ```

You should see the output from both the standalone Python function and the class method in your console. This setup allows you to call Python code directly from your .NET application using CSnakes. 