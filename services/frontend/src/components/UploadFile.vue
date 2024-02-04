<template>
  <div class="uploadImageBtnContainer">

    <div class="file-input-wrapper"> 

      <input
        type="file"
        ref="fileInput"
        @input="pickFile"
        @change="uploadFile"
        id="uploadFile"
        hidden
      />
      <label for="uploadFile" class="uploadImageBtn" @click="soundEffect">Tải ảnh lên</label>
    </div>
  </div>
</template>

<script>
const sound = require('../assets/upload.mp3');

export default {
  name: "UploadFile",
  data() {
    return {
      previewImage: null,
      uploaded: false,
      initImage: null,
      image: {}
    };
  },
  props: {
    initFile: File
  },

  methods: {
    soundEffect() {
      let audio = new Audio(sound);
audio.play();
    },
    selectImage() {
      this.$refs.fileInput.click();
    },
    pickFile() {
      let input = this.$refs.fileInput;
      let file = input.files;
      console.log('file: ', file);
      if (!file[0].type.includes("image/")) {
        alert("Vui lòng chọn file có định dạng hình ảnh!");
        this.$emit("invalidType", true);
        return;
      }


      if (file && file[0]) {
        let reader = new FileReader();
        reader.onload = (e) => {
          this.previewImage = e.target.result;
        
          this.$emit("image-uploaded", e.target.result);
        };
        reader.readAsDataURL(file[0]);
        this.$emit("input", file[0]);
      }
    },

    uploadFile(event) {
      const file = event.target.files[0];
      this.$emit("file-uploaded", file);
      this.$emit("reset", true);
      this.$emit("predictClick", false);
      this.uploaded = true;
    },
  },
};
</script>

<style>
.imagePreviewWrapper {
  width: 410px;
  height: 410px;
  display: block;
  cursor: pointer;
  margin: 30px auto 30px auto;
  background-size: cover;
  background-position: center center;
  border-radius: 25px;
}

.file-input-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}

.custom-file-input-button {
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

}

.file-input {
  position: absolute;
  font-size: 100px;
  right: 0;
  top: 0;
  opacity: 0;
  cursor: pointer;
}

.uploadImageBtn {
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
  cursor: pointer;  
}

.uploadImageBtn:hover {
  background-color: #014618;
}
</style>
