
QUnit.test("errors should be hidden on keypress", function (assert) {
  $('input[name="text"]').trigger('keypress');
  assert.equal($('.has-error').is(':visible'), false);
});

QUnit.test("errors aren't hidden if there is no keypress", function (assert) {
  assert.equal($('.has-error').is(':visible'), true);
});
