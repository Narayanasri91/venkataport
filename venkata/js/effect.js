$( document ).ready(function() {

    function hide_all() {
	$("#row2").hide();
	$("#row1").hide();
	$("#row4").hide();
	$("#row3").hide();
	$("#row5").hide();
	$("#row6").hide();
    }
    function make_active(obj)
    {
    $('.navbar-inner .nav > li').removeClass('active');
    $(obj).addClass('active'); 	
    }

	hide_all();
	$("#row1").show();
     $("#row1").load("html/row1.html");

     $("#prof").click(function() {
	make_active(this)
	hide_all();
	$("#row1").show();
     $("#row1").load("html/row1.html");
	});

$("#proj").click(function() {
	make_active(this)
	hide_all();
	$("#row2").show();
	$("#row2").load("html/row2.html");

	});

$("#cert").click(function() {
	make_active(this)
	hide_all();
	$("#row3").show();
     $("#row3").load("html/row3.html");
	});

$("#vir").click(function() {
	make_active(this)
	hide_all();
	$("#row4").show();
     $("#row4").load("html/row4.html");
	});

$("#con").click(function() {
	make_active(this)
	hide_all();
	$("#row5").show();
     $("#row5").load("html/row5.html");
	});

$("#fed").click(function() {
	make_active(this)
	hide_all();
	$("#row6").show();
     $("#row6").load("html/row6.html");
	});
$("#link1").click(function() {
alert("clicked")
	});


});

function reset_entr(){

    document.getElementById("row6_form").reset();
}
function remove_entry() {
    var x = document.getElementById("sel1");
    div_val = x.value;
    x.remove(x.selectedIndex);
    $('#'+div_val).show();
    $('#'+div_val).accordion();
}

function show_range(val) {
      document.getElementById('input_ran').value=val; 
}