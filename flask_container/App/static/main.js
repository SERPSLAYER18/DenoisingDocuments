//========================================================================
// Drag and drop image handling
//========================================================================

var fileDrag = document.getElementById("file-drag");
var fileSelect = document.getElementById("file-upload");

// Add event listeners
fileDrag.addEventListener("dragover", fileDragHover, false);
fileDrag.addEventListener("dragleave", fileDragHover, false);
fileDrag.addEventListener("drop", fileSelectHandler, false);
fileSelect.addEventListener("change", fileSelectHandler, false);

function fileDragHover(e) {
    // prevent default behaviour
    e.preventDefault();
    e.stopPropagation();

    fileDrag.className = e.type === "dragover" ? "upload-box dragover" : "upload-box";
}

function fileSelectHandler(e) {
    // handle file selecting
    var files = e.target.files || e.dataTransfer.files;
    fileDragHover(e);
    for (var i = 0, f; (f = files[i]); i++) {
        previewFile(f);
    }
}

//========================================================================
// Web page elements for functions to use
//========================================================================

//var imagePreview = document.getElementById("image-preview");
var imageDisplay = document.getElementById("image-preview");
var uploadCaption = document.getElementById("upload-caption");
var predResult = document.getElementById("pred-result");
var loader = document.getElementById("loader");
var denoisedImage = document.getElementById("denoised-image");
var fileUpload = document.getElementById("file-upload-box");
var imagePreviewDiv = document.getElementById("image-preview-div");
var imageDenoisedDiv = document.getElementById("image-denoised-div");
var downloadResultButton = document.getElementById("download-result-btn");
var recognizedTextBox = document.getElementById("recognized_text_box");
var recognizedText = document.getElementById("recognized_text");
//========================================================================
// Main button events
//========================================================================

function submitImage() {
    // action for the submit button
    console.log("submit");

    if (!imageDisplay.src) {
        window.alert("Please select an image before submit.");
        return;
    }

    show(loader)
    imageDisplay.classList.add("loading");
    hide(uploadCaption)
    //hide(imagePreview)

    // call the predict function of the backend
    predictImage(imageDisplay.src);
}

function clearImage() {
    // reset selected files
    fileSelect.value = "";

    // remove image sources and hide them
    //imagePreview.src = "";
    imageDisplay.src = "";
    denoisedImage.src = "";
    recognizedText.innerHTML = "";

    //hide(imagePreview);
    hide(imageDisplay);
    hide(loader);
    hide(denoisedImage);
    hide(imagePreviewDiv);
    hide(imageDenoisedDiv);
    hide(downloadResultButton);
    hide(recognizedTextBox)
    show(uploadCaption);
    show(fileUpload)

    imageDisplay.classList.remove("loading");
}

function previewFile(file) {
    // show the preview of the image
    console.log(file.name);
    var fileName = encodeURI(file.name);

    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = () => {
        //imagePreview.src = URL.createObjectURL(file);

        // show(imagePreview);

        // reset
        //predResult.innerHTML = "";
        imageDisplay.classList.remove("loading");

        displayImage(reader.result, "image-preview");
        console.log(reader.result)

        hide(uploadCaption);
        hide(fileUpload)
        show(imagePreviewDiv);
    };
}

//========================================================================
// Helper functions
//========================================================================

function predictImage(image) {
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(image)
    })
        .then(resp => {
            if (resp.ok)
                resp.json().then(data => {
                    displayResult(data);
                });
        })
        .catch(err => {
            console.log("An error occured", err.message);
            window.alert("Oops! Something went wrong.");
        });
}

function displayImage(image, id) {
    // display image on given id <img> element
    let display = document.getElementById(id);
    display.src = image;
    show(display);
}

function displayResult(data) {
    // display the result
    // imageDisplay.classList.remove("loading");
    hide(loader);
    recognizedText.innerHTML = data.recognized_text;
    denoisedImage.src = data.denoised_img
    show(imageDenoisedDiv);
    show(denoisedImage)
    show(downloadResultButton)
    show(recognizedTextBox)
    //show(predResult);
}


function hide(el) {
    // hide an element
    el.classList.add("hidden");
    el.classList.add("is-hidden");
}

function show(el) {
    // show an element
    el.classList.remove("hidden");
    el.classList.remove("is-hidden");
}