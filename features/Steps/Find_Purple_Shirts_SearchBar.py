from behave import *

@when('I search for purple t shirts via the searchbar')
def step_impl(context):
    #Click on search box and send 'purple shirts' with a press of return.
    context.basePageObject.set_text('Class', "search-box", "purple shirt")

