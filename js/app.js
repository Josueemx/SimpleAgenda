var toggle = 1;
$(document).ready(function(){
    $("#contacts").click(function(){
        if(toggle==1){
            var toggle = 0;
            $("#book").slideToggle();
            $("#arrow").slideToggle();
            /*$("#myForm").css("display","none");
            $("#myTable").css("display","block");*/
            $("#myTable").slideToggle(function(){
               $("#myForm").slideToggle(); 
            });
        }
        else{
            var toggle = 1;
            $("#arrow").slideToggle();
            $("#book").slideToggle();
            /*$("#myForm").css("display","block");
            $("#myTable").css("display","none");*/
            $("#myForm").slideToggle(function(){
               $("#myTable").slideToggle(); 
            });
        }
    });
});

function getData(row){
    var table = document.getElementById('myTable');
    var rowLength = table.rows.length+1;
    for (i = 0; i < rowLength; i++){
       var oCells = oTable.rows.item(i).cells;
       var cellLength = oCells.length;

       //loops through each cell in current row
       for(var j = 0; j < cellLength; j++){
          /* get your cell info here */
          /* var cellVal = oCells.item(j).innerHTML; */
       }
    }
}