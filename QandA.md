# Q&A - Common Issues and Solutions

## Q: How do I organize Python files in subdirectories?

**Problem:** You want to keep Python files in a subdirectory (e.g., `python-scripts/`) instead of the project root, but CSnakes can't find the modules.

**Error:** `ModuleNotFoundError: No module named 'YourModule'`

**Solution:**
1. **Update your .csproj file** to reference Python files in the subdirectory:
   ```xml
   <ItemGroup>
     <AdditionalFiles Include="python-scripts/ScriptDemo.py">
       <CopyToOutputDirectory>Always</CopyToOutputDirectory>
     </AdditionalFiles>
     <AdditionalFiles Include="python-scripts/Greeter.py">
       <CopyToOutputDirectory>Always</CopyToOutputDirectory>
     </AdditionalFiles>
   </ItemGroup>
   ```

2. **Add the subdirectory to Python's sys.path** in your Program.cs:
   ```csharp
   using System.Collections.Generic;
   using CSnakes.Runtime.Python;

   // Add this after getting the IPythonEnvironment
   var pythonScriptsPath = Path.Join(Environment.CurrentDirectory, "python-scripts");
   env.Execute($"import sys\nsys.path.insert(0, '{pythonScriptsPath.Replace("\\", "/")}')", 
               new Dictionary<string, PyObject>(), new Dictionary<string, PyObject>());
   ```

3. **Clean and rebuild** your project:
   ```bash
   dotnet clean && dotnet build
   ```

**Why this works:** CSnakes generates C# code based on Python files, but Python's import system needs to know where to find modules. Adding the subdirectory to `sys.path` tells Python where to look for your modules.

## Q: My Python files import each other - will this work in subdirectories?

**Answer:** Yes! Once you add the subdirectory to `sys.path`, Python files can import each other normally using relative imports (e.g., `from Greeter import Greeter`).

## Q: Do I need to keep Python files in the project root?

**Answer:** No. After configuring the subdirectory properly, you can safely remove Python files from the project root. The application will work entirely from the subdirectory. 