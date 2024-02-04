<template>
    <div class="files-input-wrapper">
      <input
        multiple
        type="file"
        @change="uploadFiles"
        id="uploadFiles"
        hidden
      />
<label for="uploadFiles" class="uploadImagesBtn" @click="soundEffect">Tải ảnh lên</label>

    </div>
</template>

<script>
const sound = require('../assets/upload.mp3');

export default {
  name: "UploadFiles",
  data() {
    return {
      images: [],
      previewImages: [],
      files: [],
      uploaded: false,
      imageFiles: []
    };
  },

  methods: {
    soundEffect() {
      let audio = new Audio(sound);
audio.play();
    },
    uploadFiles(e) {
      var files = e.target.files || e.dataTransfer.files;

      if (!files.length) return;
      for (var index = 0; index < files.length; index++) {
        var reader = new FileReader();
        reader.readAsDataURL(files[index]);
        const file = files[index];
        reader.onload = function (event) {

          const imageUrl = event.target.result;
          this.images.push({
            file: file,
            image: imageUrl});
          
        }.bind(this);
                
        console.log('files[index]: ', files[index]);


      }
      this.$emit("files-uploaded", files);
      this.$emit("images", this.images);
      this.$emit("reset", true);
      this.$emit("createClick", false);

      this.files = files;

      this.uploaded = true;
    },
    createImage(files) {
      var vm = this;
      for (var index = 0; index < files.length; index++) {
        var reader = new FileReader();
        reader.onload = function (event) {
          const imageUrl = event.target.result;
          console.log('imageUrl: ', event.target);
          vm.images.push({image: imageUrl, width: '', height: ''});
        };
        reader.readAsDataURL(files[index]);
      }
      this.$emit("files-uploaded", files);
      this.$emit("images", this.images);
      this.$emit("reset", true);
      this.$emit("createClick", false);

      this.files = files;
      console.log("this.images: ", this.images);

      this.uploaded = true;
    },
    removeImage(index) {
      this.images.splice(index, 1);
    },
  },
};
</script>

<style>


.files-input-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}

.custom-files-input-button {
  display: block;
  margin-left: auto;
  margin-right: auto;
  background-color: #184226;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  font-size: 24px;
  margin-top: 10px;
}

.files-input {
  position: absolute;
  height: 50px;
  width: 200px;
  /* font-size: 50px; */
  right: 0;
  top: 0;
  opacity: 1;
  cursor: pointer;
  background-color: red;
}





.uploadImagesBtn {
  display: inline-block;
  padding: 0.5rem;

  margin-left: auto;
  margin-right: auto;
  background-color: #006c24;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: 'AR One Sans';
  font-size: 24px;
  /* margin-top: 10px; */
  cursor: pointer;  
}

.uploadImagesBtn:hover {
  background-color: #015b1f;
}
</style>
