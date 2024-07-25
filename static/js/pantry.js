

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


    // $('#save-btn').click(function() {
    //     localStorage.setItem("scrollPosition", window.scrollY);
    // });

    // if (localStorage.getItem("scrollPosition") !== null) {
    //     window.scrollTo(0, localStorage.getItem("scrollPosition"));
    //     localStorage.removeItem("scrollPosition");
    // }

    $("#add-item-btn").click(toggleAddItem);
    $("#cancelAddItem").click(toggleAddItem);

    $(".pantry-item-container span").click(function(){
        const itemId = $(this).data("item-id");
        const itemName = $(this).data("item-name");
        const itemQuantity = $(this).data("item-quantity");
        const itemUnit = $(this).data("item-unit");
        const itemExpiration = $(this).data("item-expiration");

        $("nav").fadeOut();
        $("#edit-form").fadeIn();

        $("#edit-id").val(itemId)
        $("#edit-name").val(itemName).css({"text-transform":"capitalize"});
        $("#edit-quantity").val(Number(itemQuantity));
        $("#edit-unit").val( (itemUnit === "None") ? "" : itemUnit );
        $("#edit-expiration").val(convertedDateFormat(itemExpiration)); 
  
    });

    $("#edit-back-btn").click(function(){
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

function convertedDateFormat(dateString) {

    const date = new Date(dateString);

    const year = date.getFullYear();
    const month = ('0' + (date.getMonth() + 1)).slice(-2); // Months are zero-indexed
    const day = ('0' + date.getDate()).slice(-2);

    return `${year}-${month}-${day}`;
}

