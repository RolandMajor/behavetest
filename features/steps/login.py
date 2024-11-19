from behave import *
from hamcrest import assert_that, equal_to


@given("the home page is opened")
def step_impl(context):
    context.homepage.open_page()


@given("the '{field}' field is filled with '{text}'")
def step_impl(context, field, text):
    field = '' if field == '[blank]' else field
    text = '' if text == '[blank]' else text
    context.homepage.fill_out_field(field, text)


@when("the '{button}' button is clicked")
def step_impl(context, button):
    context.homepage.click_button(button)


@then("the '{error}' message is shown")
def step_impl(context, error):
    assert_that(context.homepage.get_error_message(), equal_to(error))
