

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

    $("#add-item-btn").click(toggleAddItem);
    $("#cancelAddItem").click(toggleAddItem);
    $(".delete").click(toggleDeleteCOnfirmation);

});

function toggleAddItem(event){
    event.preventDefault();

    const $addItemForm = $("#add-item-form");
    const $addItemBtn = $("#add-item-btn");

    if ($addItemForm.css("display") === "none") {
        $addItemForm.slideDown();
        $addItemBtn.css({"display":"none"});
    } else {
        $addItemForm.slideUp();
        $addItemBtn.fadeIn();
    }
}

function toggleDeleteCOnfirmation(event){
    event.preventDefault();

    console.log("CLICKED")

    const $deleteItemConfirmation = $("#delete-message-form");

    if ($deleteItemConfirmation.css("display") === "none") {
        $deleteItemConfirmation.fadeIn();
    } else {
        $deleteItemConfirmation.fadeOut();
    }
}

