$(document).ready(function(){
	resetDate();

	$("#menu-toggle").on('click',function(){
		$("#menu-toggle").toggleClass("active");
		$('#theMenu').toggleClass('menu-open');
	});

	$("#older-btn").click(function(){
		var date = $("h2.hdate").text();
		$.ajax({
			url:'/older/'+date,
			type:'POST',
			dataType:'json',
			success:function(data){
				if(data.result=="None"){
					alert("亲，没有更早的文章了！");
				}else if(data.result=="Fail"){
					alert("亲，出错了，赶快叫你亲爱的来debug吧！");
				}else{
					display_post(data);
				}
			},
			fail:function(){

			}
		});
	});

	$("#random-btn").click(function(){
		var pid = $("#pid").text();
		$.ajax({
			url:'/random/'+pid,
			type:'POST',
			dataType:'json',
			success:function(data){
				if(data.result=="None"){
					alert("亲，没有别的文章了！");
				}else{
					display_post(data);
				}	
			},
			fail:function(data){

			}
		});
	});

	$("#today-btn").click(function(){
		$.ajax({
			url:'/today',
			type:'POST',
			dataType:'json',
			success:function(data){
				if(data.result=="None"){
					alert("你家亲爱的太懒，今天还什么都没写饿！");
				}else{
					display_post(data);
				}
			},
			fail:function(data){

			}
		});
	});

	function display_post(post){
		var date = new Date(post.datetime.$date);
		var width = 400;
		$("div.entry").fadeOut(1000,function(){
			date.setHours(date.getHours()-8)
			$("h2.date").text(jQuery.timeago(date));
			$("span.weekday_text").text(post.weekday);
			$("div.text").html(post.content);
			$("h2.hdate").text(date.getFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate());
			if(post._id!=undefined){
				$("#pid").text(post._id.$oid);
			}else{
				$("#pid").text('None');
			}
		});
		$("div.entry").fadeIn(1000);

	}

	function resetDate(){
		var date = $("h2.date").text();
		date = date.replace(/a.m./,"am");
		date = date.replace(/p.m./,"pm");
		$("h2.date").text(jQuery.timeago(date));
	}


});