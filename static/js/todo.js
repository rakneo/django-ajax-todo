

function createPost() {
    console.log("Create Post Function Called");
     $.ajax({
        url: "create/",
        type: "POST",
        data: {todo_event:$('#todo-input').val()},

        success: function (json) {
            $("#todo-input").val('');
            console.log('success');
            $("#sortable").html(json.html_data);
        },
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });


}

function completeEvent(url) {

    console.log("completeEvent Called");
    $.ajax({
        url: url,
        type: "get",
        success: function (json) {
            $("#done-items").html(json.html_data1);
            $("#sortable").html(json.html_data2);
            console.log(json)

        },

        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }

    });

}

function deleteEvent(url) {

    console.log("deleteEvent Called");
    $.ajax({
        url: url,
        type: "get",
        success: function (json) {
            $("#done-items").html(json.html_data);
            console.log(json)

        },

        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }

    });

}

// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!") ; // sanity check
    createPost();
});

//$('#post-form').off('submit');

$('.not-done').on('click', '#completed_check', function () {
    console.log("Complete Button Clicked");
    var url = $(this).attr('data-url');
    console.log(url);
    completeEvent(url);
    console.log("Success");
});

//$('#completed_check').off('click');

$('.completed').on('click', '#btn-delete',function () {
    console.log("Delete Button Clciked");
    var url = $(this).attr('data-url');
    console.log(url);
    deleteEvent(url);
    console.log("Success");
});

//$('#btn-delete').off('click');
