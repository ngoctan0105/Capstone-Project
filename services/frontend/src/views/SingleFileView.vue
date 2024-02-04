<template>
  <Transition  appear mode="out-in">
  <div class="singleFilePage">
    <HeaderComponent />

    <div class="uploadComponent" v-if="!uploadedImage">
      <p class="uploadQuote">
        Tải lên một ảnh lá cây <br />
        và chờ xem kết quả
      </p>

      <UploadFile         @file-uploaded="handleFileUploaded"
      @image-uploaded="handleImageUploaded"
        
        @reset="afterUpload"
        @predictClick="afterUpload1"
        class="uploadFileInit"
        />

      <img src="../assets/upload.gif" class="uploadGif" />
      <CategoriesComponent class="categoriesUpload" />
    </div>
    <Transition  appear mode="out-in">
    <div class="singleFilePageBody" v-if="uploadedImage">

      <div class="imageContainer">
        <div class="imageBackground">
        <img v-if="height > width" :src="uploadedImage" ref="image" @load="getImageSize" class="verticalImage">
        <img v-else-if="height < width" :src="uploadedImage" ref="image" @load="getImageSize" class="horizontalImage">
        <img v-else :src="uploadedImage" ref="image" @load="getImageSize" class="squareImage">

      </div>
        <UploadFile         @file-uploaded="handleFileUploaded"
      @image-uploaded="handleImageUploaded"
        
        @reset="afterUpload"
        @predictClick="afterUpload1" 
        @invalidType="handleInvalidType"
        
        />
      </div>
      <div class="textContainer">
        <PredictBtn
          :imageFile="file"
          
          @plantDiseaseObj="handleResult2"
          @predictClick="predictClick = true"
          @reset="afterShowResult"
          @confidence="handleResult1"
          v-if="uploadedImage && !predictClick && !invalidType"
        />
        <div class="textContainerBody" v-if="predictClick && !reset">
          <Transition  appear mode="out-in">
          <PredictionComponent
            :plantDiseaseObj="plantDiseaseObj"
            
            v-if="predictClick && !reset && confidence >= 0.5"
          />
          <div v-if="predictClick && !reset && confidence < 0.5" class="undefined">
            <p>Không thể xác định được loại cây và tình trạng của cây.<br>Vui lòng chọn ảnh khác!</p>
            <img src="../assets/undefined.gif" >
            </div>
          </Transition>
        </div>
      </div>
    </div>
  </Transition>
  </div>
</Transition>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import UploadFile from "@/components/UploadFile.vue";
import PredictBtn from "@/components/PredictBtn.vue";
import PredictionComponent from "@/components/PredictionComponent.vue";
import CategoriesComponent from "@/components/CategoriesComponent.vue";
import { Transition } from "vue";

export default {
  name: "SingleFileView",
  components: {
    HeaderComponent,
    UploadFile,
    PredictBtn,
    PredictionComponent,
    CategoriesComponent,
    Transition
  },

  data() {
    return {
      uploadedImage: null,
      file: null,
      imageUrl: "",
      plantDiseaseObj: null,
      confidence: 0,
      suggestClick: false,
      predictClick: false,
      reset: true,
      init: false,
      height: '',
                    width: '',
                    isSingle: true,
      invalidType: false
    };
  },
  methods: {

    getImageSize() {
                    const img = new Image();
                    console.log('this.$refs.image.src: ', this.$refs.image.src);
                    img.src = this.$refs.image.src;
                    img.onload = () => {
                        this.width = img.width;
                        this.height = img.height;
                        console.log('size: ', this.width + ' ' + this.height);
                    };
                    
                },
    handleInvalidType(invalidType) {
      this.invalidType = invalidType;
      location.reload();
    },

    handleFileUploaded(file) {
      this.file = file;
    },
    handleImageUploaded(image) {
      this.uploadedImage = image;
    },
    handleResult1(confidence) {
      this.confidence = confidence;
    },
    handleResult2(plantDiseaseObj) {
      this.plantDiseaseObj = plantDiseaseObj.data;
      this.reset = true;
    },
    afterUpload(reset) {
      this.reset = reset;
    },
    afterUpload1(predictClick) {
      this.predictClick = predictClick;
    },
    afterShowResult(reset) {
      this.reset = reset;
      console.log("this.reset: ", this.reset);
      localStorage.removeItem('imageUrl');
    },

    uploadFile(e) {
            const file = e.target.files[0];
      console.log('file: ', file.type);
      if (!file.type.includes("image/")) {
        alert("Vui lòng chọn file có định dạng hình ảnh!");
        return;
      }
      else {
        this.createImage(file);
      }


      this.uploadedImage = file;
    },
    createImage(file) {

      var reader = new FileReader();
      reader.onload = function (event) {
        const imageUrl = event.target.result;
        this.imageUrl = imageUrl;
        localStorage.setItem('imageUrl', imageUrl);
      };
      reader.readAsDataURL(file);
      this.file = file;
      this.init = true;

    },
  },
};
</script>

<style>
.singleFilePageBody {
  display: inline-flex;
  position: absolute;
  top: 80px;
  left: 40px;
}

.imageContainer {
  height: 560px;
  width: 460px;
  background-color: #f9f7e5;
  border-radius: 25px;
  align-self: flex-end;
  margin-right: 70px;

}

.imageBackground {
  width: 410px;
  height: 410px;
  display: flex;
  margin: 30px auto 30px auto;
  background-size: cover;
  background-position: center center;
  border-radius: 25px;  
  background-color: black;
}

.squareImage {
  width: 100%;
  height: 100%;
  border-radius: 25px;  

}

.verticalImage {
  height: 100%;
  margin-left: auto;
  margin-right: auto; 
}

.horizontalImage {
  width: 100%;
  align-self: center;
  justify-self: center;
}

.textContainer {
  height: 640px;
  width: 760px;
  background-color: #d5e6d8;
  border-radius: 25px;
  align-self: flex-end;
  display: flex;
  place-items: center;
}

.textContainerBody {
  background-color: white;
  border-radius: 25px;
  height: 600px;
  width: 720px;
  padding: 20px;
  margin-left: auto;
  margin-right: auto;  

}

.propose-btn {
  display: block;
  background-color: blue;
  color: white;
  cursor: pointer;
  padding: 5px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 5px;
}

.undefined {
  font-family: "Aleo";
  font-weight: 600;
  font-size: 18px;
  margin-top: 10px;
  font-style: italic;
}

.undefined img {
  margin-top: 5px;
}

.uploadFileInit {
  margin-top: 10px;
}

.entering {
    animation: added 1s;
  }
</style>
