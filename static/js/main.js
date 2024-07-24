

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


    $('#save-btn').click(function() {
        localStorage.setItem("scrollPosition", window.scrollY);
    });

    if (localStorage.getItem("scrollPosition") !== null) {
        window.scrollTo(0, localStorage.getItem("scrollPosition"));
        localStorage.removeItem("scrollPosition");
    }

    $("#add-item-btn").click(toggleAddItem);
    $("#cancelAddItem").click(toggleAddItem);
    // $(".delete").click(toggleDeleteConfirmation);


    $(".pantry-item-container span").click(function(){
        const itemName = $(this).data("item-name");
        const itemId = $(this).data("item-id");
        const itemQuantity = $(this).data("item-qty");

        $("nav").fadeOut();
        $("#edit-form").fadeIn();
        $("#edit-form h2 span").text(itemName);
    });

    $("#edit-back-btn, #edit-save-btn").click(function(){
        $("nav").fadeIn();
        $("#edit-form").fadeOut();
    });

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

// function toggleDeleteConfirmation(event){
//     event.preventDefault();

//     const $deleteItemConfirmation = $("#delete-message-form");

//     if ($deleteItemConfirmation.css("display") === "none") {
//         $deleteItemConfirmation.fadeIn();
//     } else {
//         $deleteItemConfirmation.fadeOut();
//     }
// }

