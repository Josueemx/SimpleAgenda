
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
    /*lo de abajo se puede hacer con ajax aqui ver*/
    var name = $('#myTable tr:nth-child('+id+') td:nth-child(1)').text();
    var lastname = $('#myTable tr:nth-child('+id+') td:nth-child(2)').text();
    var email = $('#myTable tr:nth-child('+id+') td:nth-child(3)').text();
    var phone = $('#myTable tr:nth-child('+id+') td:nth-child(4)').text();
    var phone_type = $('#myTable tr:nth-child('+id+') td:nth-child(5)').text();
    var address = $('#myTable tr:nth-child('+id+') td:nth-child(6)').text();
    $("#id").val(id);
    $("#name").val(name);
    $("#lastname").val(lastname);
    $("#email").val(email)
    $("#phone").val(phone);
    $("#phone_type").val(phone_type);
    $("#address").val(address);   
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