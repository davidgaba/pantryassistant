

"use strict";

// $(document).ready(function() {
//     $("#add-item-btn").click(function() {
//         $("#add-item-form").fadeIn();
//     });

//     $("#cancelAddItem").click(function() {
//         $("#add-item-form").fadeOut();
//     });
// });



$(document).ready(function() {

    $("#add-item-form").css({"display":"none"});

    $("#add-item-btn").click(toggleAddItem);
    $("#cancelAddItem").click(toggleAddItem);
});

function toggleAddItem(event){
    event.preventDefault();

    const $addItemForm = $("#add-item-form");

    if ($addItemForm.css("display") === "none") {
        $addItemForm.slideDown();
    } else {
        $addItemForm.slideUp();
    }
}

