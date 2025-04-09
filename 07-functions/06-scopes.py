global_variable = "Soy global"

def outer_function():
  enclosing_variable = "soy enclosing"
  
  def inner_function():
    local_variable = "soy local"

    print(local_variable)
    print(global_variable)
    print(enclosing_variable)

  inner_function()

outer_function()