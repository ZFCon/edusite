//returns cookie from browser- from Django docs link below
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split('console.log(data);;');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//also from docs-
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
  
var csrftoken = getCookie('csrftoken');
  //set csrf token
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
  //now your ajax logic as usual


$('#studentForm').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")
    create_student();
});


// AJAX for StudentForm
function create_student() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "inst/student/add", // the endpoint
        type : "POST", // http method
        data : { 
            csrf : $('input[name="csrfmiddlewaretoken"]').val(),
            std_inst : $('#std-inst').val(), 
            std_sch : $('#std-sch').val(),
            std_dept : $('#std-dept').val(),
            std_dptcls : $('#std-dptcls').val(),
            std_abbr : $('#std-abbr').val(),
            std_fname : $('#std-fname').val(),
            std_lname : $('#std-lname').val()

        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#std-inst').val(''); // remove the value from the input
            $('#std-sch').val(''); 
            $('#std-dept').val(''); 
            $('#std-dptcls').val(''); 
            $('#std-abbr').val(''); 
            $('#std-fname').val(''); 
            $('#std-lname').val(''); 
            console.log(json); // log the returned json to the console
            $("#std-list").prepend('<tr><td>'+json.sabbr+'</td><td>'+json.sfname+'</td><td></td><td>'+json.sdptcls+'</td><td>'+json.sinst+'</td><td></td><td class="text-right"><div class="btn-group"><button class="btn-white btn btn-xs">View</button><button class="btn-white btn btn-xs">Edit</button><button class="btn-white btn btn-xs">Delete</button></div></td></tr>');
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// AJAX for posting
function delete_post(post_primary_key){
    if (confirm('are you sure you want to remove this post?')==true){
        $.ajax({
            url : "/inst/HKUST/SENG/ECE/DelCourse/", // the endpoint
            type : "POST", // http method
            data : { crseid : post_primary_key }, // data sent with the delete request
            success : function(json) {
                // hide the post
              $('#post-'+post_primary_key).hide(); // hide the post on success
              console.log("post deletion successful");
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                $('#results').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    } else {
        return false;
    }
};

// AJAX for posting
function edit_post(post_primary_key) {
    console.log("edit post is working!") // sanity check
    $.ajax({
        url : "/inst/HKUST/SENG/ECE/EditCourse/",
        type : "POST",
        data : { crseid : post_primary_key },
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        error : function(xhr,errmsg,err) {
            // Show an error
            $('#results').html("<div class='alert-box alert radius' data-alert>"+
            "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }

    })
};
