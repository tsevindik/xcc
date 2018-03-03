(function($){
	var csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
	var trade_prices_check = $("input[name=trade_prices_check]").val();
	var get_rate_icon = function(val){
		var clss = '<i class="fa fa-sort-down"></i>';
		if (val > 0) {
			clss = '<i class="fa fa-sort-up"></i>';
		} else if (val == 0) {
			clss = '<i class="fa fa-minus"></i>';
		}
		return clss;
	}
	var get_color = function(val){
		var clss = "danger";
		if (val > 0) {
			clss = "success";
		} else if (val == 0) {
			clss = "warning";
		}
		return clss;
	}
	window.trade_prices_func = function(){
		var limit = $("#limit_filter").val();
		var start = $("#start_filter").val();
		var search = $("#search_filter").val();
		$.ajax({
			url: trade_prices_check,
			type: "POST",
			data: {
				csrfmiddlewaretoken: csrfmiddlewaretoken,
				limit: limit,
				start: ((parseInt(start) - 1) * parseInt(limit)),
				search: search,
			},
			dataType: "json",
			beforeSend: function(){
				$("#trade_prices_list").html('<tr><td colspan="9" class="text-center"><img src="/static/assets/img/gif/animat-diamond-color.gif" style="width:30%;"></td></tr>');
			},
			success: function(data){
				var output = "";
				$.each(data, function(i, v){
					output += '<tr>';
					output += '<td>'+v.rank+'</td>';
					output += '<td><img src="https://files.bitscreener.com/static/img/coins/16x16/'+v.id+'.png" alt="'+v.id+'"> '+v.name+'</td>';
					output += '<td>'+v.market_cap_usd+'</td>';
					output += '<td>'+v.price_usd+'</td>';
					output += '<td>'+v.available_supply+'</td>';
					output += '<td>'+v["24h_volume_usd"]+'</td>';
					output += '<td class="table-'+get_color(v.percent_change_1h)+
						' text-'+get_color(v.percent_change_1h)+'">'+get_rate_icon(v.percent_change_1h)+' '+(v.percent_change_1h ? v.percent_change_1h : main_trans["unknown"])+'</td>';
					output += '<td class="table-'+get_color(v.percent_change_24h)+
						' text-'+get_color(v.percent_change_24h)+'">'+get_rate_icon(v.percent_change_24h)+' '+(v.percent_change_24h ? v.percent_change_24h : main_trans["unknown"])+'</td>';
					output += '<td class="table-'+get_color(v.percent_change_7d)+
						' text-'+get_color(v.percent_change_7d)+'">'+get_rate_icon(v.percent_change_7d)+' '+(v.percent_change_7d ? v.percent_change_7d : main_trans["unknown"])+'</td>';
					output += '</tr>';
				});
				$("#trade_prices_list").html(output);
				$("#trade_count").html(data.length);
			}
		});
	}
	trade_prices_func();
	setTimeout(trade_prices_func, 5000);
	$("#start_filter, #limit_filter, #search_filter").on("change keyup paste", function(){trade_prices_func();});
})(jQuery);