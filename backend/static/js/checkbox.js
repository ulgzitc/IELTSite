var checks = document.querySelectorAll(".form-check-input-checkbox");
var max = 2;
for (var i = 0; i < checks.length; i++) {
    checks[i].onclick = selectiveCheck;
}
function selectiveCheck(event) {
    var checkedChecks = document.querySelectorAll(".form-check-input-checkbox:checked");
    if (checkedChecks.length > max) {
        alert("You can only select a maximum of " + max + " options.");
        this.checked = false;
    }
}