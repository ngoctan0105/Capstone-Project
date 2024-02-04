<template>
  <Transition  appear mode="out-in">
  <div class="multipleFilesPage">
    <HeaderComponent />

    <div v-if="!detail">

    <div class="uploadComponent" v-if="uploadedImages.length == 0">
      <p class="uploadQuote">
        Tải lên nhiều ảnh lá cây <br />
        và chờ xem kết quả
      </p>

      <UploadFiles
        @files-uploaded="handleFilesUploaded"
        @images="handleImagesUploaded"
        @reset="afterUpload"
        @createClick="afterUpload1"
        @imageFiles="handleImageFiles"
        class="uploadFilesInit"
      />

      <img src="../assets/upload.gif" class="uploadGif" />
      <CategoriesComponent class="categoriesUpload" />
    </div>
    <Transition  appear mode="out-in">
    <div class="multipleFilesPageBody" v-if="uploadedImages.length != 0">
      <div class="listContainer">
        <UploadFiles
          @files-uploaded="handleFilesUploaded"
          @images="handleImagesUploaded"
          @reset="afterUpload"
          @createClick="afterUpload1"
          @imageFiles="handleImageFiles"
          class="uploadFiles"
        />

        <div style="overflow-y: auto; max-height: 440px">
          <ul
            v-for="(image, index) in uploadedImages"
            :key="index"
            class="imageList"
          >
            <li class="imageInList">
              <img :src="image.image" />

              <p>{{ image.file.name }}</p>
            </li>
          </ul>
        </div>
      </div>
      <div class="tableContainer">
        <CreateTableBtn
          :imageFiles="files"
          :images="uploadedImages"
          @table="handleResult"
          @createClick="
            createClick = true;
            loading = true;
          "
          @reset="afterShowResult"
          v-if="uploadedImages.length != 0 && !createClick"
        />
        <Transition appear>
          <div
            class="tableContainerBody"
            v-if="tableData.length != 0 && createClick && !reset"
          >
            <div
              class="tableContainerData"
              v-if="tableData.length != 0 && createClick && !reset"
            >
              <table class="table">
                <thead>
                  <tr>
                    <th>Ảnh</th>
                    <th>Loại cây</th>
                    <th>Tình trạng</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in tableData" :key="index" @click="showDetail(item)">
                    <td>
                      <img :src="item['Ảnh']" />
                    </td>
                    <td
                      v-if="item['Độ tin cậy'] < 0.95"
                      colspan="3"
                      style="font-style: italic"
                    >
                      Không xác định
                    </td>
                    <td v-if="item['Độ tin cậy'] >= 0.95">
                      {{ item["Loại cây"] }}
                    </td>
                    <td v-if="item['Độ tin cậy'] >= 0.95">
                        {{ item["Tình trạng"] }}
                    </td>
                  </tr>


                </tbody>



              </table>
            </div>

            <ExportCSVBtn :csv="tableData" v-if="tableData.length != 0" />
          </div>
        </Transition>
      </div>
    </div>
  </Transition>

  </div>

    <div v-else>
        <Transition  appear mode="out-in">

  <DetailView 
  :plantDiseaseObj="selectedItem"
  @showDetail="closeDetail"
  />
    </Transition>

</div>
  
  </div>
</Transition>
</template>

<script>
import { Transition } from "vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import UploadFiles from "@/components/UploadFiles.vue";
import CreateTableBtn from "@/components/CreateTableBtn.vue";
import ExportCSVBtn from "@/components/ExportCSVBtn.vue";
import CategoriesComponent from "@/components/CategoriesComponent.vue";
import DetailView from "./DetailView.vue";
const sound = require('../assets/button-click.mp3');

export default {
  name: "MultipleFilesView",
  components: {
    HeaderComponent,
    UploadFiles,
    CreateTableBtn,
    ExportCSVBtn,
    Transition,
    CategoriesComponent,
    DetailView
  },
  data() {
    return {
      uploadedImages: [],
      files: [],
      tableData: [],
      createClick: false,
      reset: true,
      loading: false,
      detailClick: false,
      init: false,
      detail: false,
      height: '',
                    width: ''
    };
  },
  methods: {
    getImageSize() {
      console.log("Image Width: ", document.querySelector("img").naturalWidth);
console.log("Image Width: ", document.querySelector("img").naturalHeight);
                    
                },

    closeDetail(showDetail) {
      this.detail = showDetail;
      this.selectedItem = null;
    },
    handleImageFiles(imageFiles) {
      this.imageFiles = imageFiles;
    },

    handleFilesUploaded(files) {
      this.files = files;
    },

    handleImagesUploaded(images) {
      this.uploadedImages = images;
    },

    handleResult(table) {
      this.tableData = table;
    },

    afterUpload(reset) {
      this.reset = reset;
    },
    afterUpload1(createClick) {
      this.createClick = createClick;
    },

    afterShowResult(reset) {
      this.reset = reset;
    },


    showDetail(item) {
      let audio = new Audio(sound);
audio.play();
      this.selectedItem = item; // Lưu thông tin của hàng được chọn
      this.detail = true;
      console.log('this.detail: ', this.detail);
    },

  },
};
</script>

<style>
.multipleFilesPageBody {
  display: inline-flex;
  position: absolute;
  top: 80px;
  left: 40px;
}

.listContainer {
  height: 560px;
  width: 400px;
  background-color: #f9f7e5;
  border-radius: 25px;
  align-self: flex-end;
  position: relative;
  overflow: hidden;
  display: inline-block;
  margin-right: 70px;
}

.loading {
  justify-self: center;
  align-self: center;
}

.tableContainer {
  height: 640px;
  width: 830px;
  background-color: rgb(238, 238, 238);
  border-radius: 25px;

  align-self: flex-end;
  place-items: center;
  display: flex;
}

.tableContainerBody {
  border-radius: 25px;
  height: 700px;
  width: 830px;
}

.tableContainerData {
  overflow-y: auto;
  max-height: 480px;
  margin-top: 80px;
}

.table {

  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
  font-family: "Alata";
}

tbody tr:nth-child(odd) {
  background-color: #f9f7e5;
}

tbody tr:nth-child(odd):hover {
  cursor: pointer;
  background-color: #faf6d3;
}

tbody tr:nth-child(even) {
  background-color: #d5e6d8;
}

tbody tr:nth-child(even):hover {
  cursor: pointer;
  background-color: #c5e4cb;
}

.table th:nth-child(1),
.table td:nth-child(1) {
  width: 100px;
  text-align: center;
  justify-items: center;
}
.table th:nth-child(2),
.table td:nth-child(2) {
  width: 150px;
  text-align: start;
}
.table th:nth-child(3),
.table td:nth-child(3) {
  width: 380px;
  text-align: start;
}


.table th:nth-child(3) {
  text-align: center;
}

.table th,
.table td {
  padding: 10px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.table th {
  background-color: #184226;
  color: white;
  position: sticky;
  top: 0;
}

.table td {
  font-weight: 500;
}

.table tr {
  border: 2px solid #ccc;
}

.table img {
  height: 50px;
  width: 50px;
  margin-left: auto;
  margin-right: auto;
  border: 3px solid #ffffff;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 2s ease, transform 2s ease-in-out;
  transform: translateY(0px);
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.uploadComponent {
  position: absolute;
  top: 270px;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
}

.uploadQuote {
  position: absolute;
  top: -100px;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: "Alata";
  font-size: 48px;
  color: black;
}

.uploadGif {
  width: 400px;
  position: absolute;
  top: 200px;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: -1;
}

.categoriesUpload {
  position: absolute;
  bottom: -520px;
  left: 50%;
  transform: translate(-50%, -50%);
}

.custom-files-input-button-init {
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
  cursor: pointer;
}

.files-input-init {
  position: absolute;
  width: 400px;
  left: 400px;
  top: 0;
  font-size: 30px;
  opacity: 1;
  cursor: pointer;
  margin-top: 10px;
}

.imageList {
  color: black;
  justify-self: center;
}

.imageInList {
  height: 100px;
  width: 360px;
  background-color: white;
  margin-bottom: 10px;
  display: flex;
  place-items: center;
  border-radius: 10px;
  padding: 10px;
  margin-left: auto;
  margin-right: auto;
}

.imageInList img {
  height: 80px;
  width: 80px;
  border-radius: 10px;
}

.imageInList button {
  place-self: start;
  margin-right: 10px;
  margin-top: 10px;
}

.imageInList p {
  font-size: 12px;
  margin-left: 10px;
  font-family: "Alata";
  text-align: start;
}

.uploadFilesInit {
  margin-top: 10px;
}

.uploadFiles {
  margin-top: 25px;
  margin-bottom: 20px;
}
</style>
