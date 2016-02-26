##Creating a new Monitor Type

- The monitor module should stay in sems.monitors module;
- The name of module should be in snake case;
- The name of class should have the "Monitor" suffix;
- The class should extend the monitor.Base class.
- Use the `@Monitor` decorator;

###The Monitor Decorator
 The first argument of decorator is a short description;
  The second argument of decorator is a dict with specific configuration fields
  for monitor;


