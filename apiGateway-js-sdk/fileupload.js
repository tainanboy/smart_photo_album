window.onload = function () {
	var sendbtn = document.getElementById('submit');
	var sendqbtn = document.getElementById('submitq');
	var image_display = document.getElementById('imageDisplay');

	// upload photo
	sendbtn.onclick = function(){
		var input = $("#fileupload").val();
		console.log(input)
		console.log('uploading file.....')
		// fileInput is an HTMLInputElement: <input type="file" id="myfileinput" multiple>
		var fileInput = document.getElementById("fileupload");
		// files is a FileList object
		var file = fileInput.files[0];
		console.log(file)
		let config = {
		headers:{'Content-Type':'multipart/form-data; boundary=${data._boundary}', "X-Api-Key":'T0zHcQNXRV5nXpROpKiSq4OPNEOuIBwb6vfwZSUb'}
		};  
		url = 'https://h0atj8ks3a.execute-api.us-east-1.amazonaws.com/TEST/ccbd-a3-b2/' + file.name;
		console.log(url);
		// http put 
		axios.put(url,file,config).then(response=>{   
			console.log(response.data);
			alert("Upload successful!");
			location.reload();
		})
	}

	// search album
	sendqbtn.onclick = function(){
		var input = $("#q").val();
		console.log(input)
		console.log(typeof input)
		console.log('processing your input')

		var apigClient = apigClientFactory.newClient({apiKey: 'T0zHcQNXRV5nXpROpKiSq4OPNEOuIBwb6vfwZSUb'});
		var params = {
			//This is where any header, path, or querystring request params go. The key is the parameter named as defined in the API
			"q":input
		};
		var body = {
			//This is where you define the body of the request
		};
		var additionalParams = {
			//If there are any unmodeled query parameters or headers that need to be sent with the request you can add them here
		};
		// call API gateway: search endpoint
		apigClient.searchGet(params, body, additionalParams).then(function(result){
			//This is where you would put a success callback
			console.log(result);
			image_display.innerHTML = '';
			if (typeof(result.data.body) == 'undefined'){
				image_display.innerHTML += 'No matching images found.';
			}else{
				// process JSON response: get image filename list
				var body = JSON.parse(result.data.body);
				var image_list = body.hits.hits;
				var image_objects_list = [];
				for (var i = 0; i < image_list.length; i++){
					image_objects_list.push(image_list[i]._source.objectKey);
				}
				image_objects_list = Array.from(new Set(image_objects_list));
				console.log(image_objects_list);
				
				var src_host = "https://s3.amazonaws.com/ccbd-a3-b2/";
				if (image_objects_list.length == 0){
					image_display.innerHTML += 'No matching images found.';
				}else{
					image_display.innerHTML += 'Here are the query results: <br>';
					for (var i = 0; i < image_objects_list.length; i++){
						src = src_host+image_objects_list[i];
						image_display.innerHTML += '<img src=' + src+' height="300" width="450"> <br>';
					}
				}
			}   
			console.log('success')
		}).catch(function(result){
		//This is where you would put an error callback
		});
	}
}
