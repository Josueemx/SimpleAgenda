
$(document).ready(function(){
    setTimeout("$('#message').fadeOut();", 4000);
    $("#book").click(function(){
        switchButtons();
        switchLayout();
    });
    $("#arrow").click(function(){
        switchButtons();
        switchLayout();
    });
    $("#close").click(function(){
        $("#arrow").slideToggle();
        $("#close").slideToggle();
        switchLayout();
        $('#myForm').attr('action', '/add');
        $("#name").val('');
        $("#lastname").val('');
        $("#email").val('')
        $("#phone").val('');
        $("#phone_type").val('Work');
        $("#address").val(''); 
        $("#action_button").val("add");
        $('#action_button').attr('title', 'add');
    });
});

function getDataFor(id){
    $("#arrow").slideToggle();
    $("#close").slideToggle();
    $('#myForm').attr('action', '/update'); 
    getRow(id)
    switchLayout();
    $("#action_button").val("save");
    $('#action_button').attr('title', 'save');
}

function switchLayout(){
    $("#myForm").toggle();
    $("#myTable").toggle();
}

function switchButtons(){
    $("#book").slideToggle();
    $("#arrow").slideToggle();
}

function getRow(id){
    var url = window.location.href;
    $.getJSON( '/getrow', {
        id: id
      }, function(row) {
            $("#id").val(id);
            $("#name").val(row.name);
            $("#lastname").val(row.lastname);
            $("#email").val(row.email)
            $("#phone").val(row.phone);
            $("#phone_type").val(row.phone_type);
            $("#address").val(row.address);  
      });
}