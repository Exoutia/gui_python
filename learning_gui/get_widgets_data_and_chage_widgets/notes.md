## Ways to get data from widgets
There are two major ways to get data from a widget
1. tkinter variables
2. get method

### get method
Lots of widgets have obvious data that the user would want to get
Hence, there is a get method
For example, entry has a get method that returns its text

- widgets can be updated with config
- ex:- `Label.config(text='some new text')`
- this is how we update the label its had a shorthand
- `Label['text'] = 'some new text'`

### tkinter variables
- tkinter has inbuilt variables that are designed to work with widgets
- they are automatically updated by a widget and they update a widget
- Altough they still store basic data like string integers & booleans