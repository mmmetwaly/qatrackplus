/**************************************************************************/
//Initialize sortable/filterable test list table data types
function init_test_collection_tables(){
	$(".test-collection-table").each(function(idx,table){

		if ($(this).find("tr.empty-table").length>0){
			return;
		}

		var cols = [
			null, //Action
			null, //Unit
			null, //Freq
			null,  // Test list name
			{"sType":"span-timestamp"}, //due date
			{"sType":"span-timestamp"}, //date completed
			null, //qa status
			null//assigned to
		];

		var	filter_cols = [
				null, //action
				{type: "select"}, //Unit
				{type: "select"}, //Freq
				{type: "text" }, // Test list name
				{type: "text" }, //due date
				{type: "text" }, //date completed
				null, //qa status
				{type: "select"}//assigned to
			];


		$(table).dataTable( {
			sDom: "t",
			bStateSave:false, //save filter/sort state between page loads
			bFilter:true,
			bPaginate: false,
			aaSorting:[[3,"asc"]],//sort by name
			aoColumns: cols,
			fnAdjustColumnSizing:false

		}).columnFilter({
			sPlaceHolder: "head:after",
			aoColumns: filter_cols
		});

		$(table).find("select, input").addClass("input-small");

	});

}

/**************************************************************************/
$(document).ready(function(){
	init_test_collection_tables();
});

