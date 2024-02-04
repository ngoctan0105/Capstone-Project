<template>
  <button @click="create" class="create-btn">Xem kết quả</button>
</template>

<script>
import axios from "axios";
const sound = require('../assets/result.mp3');

export default {
  name: "CreateTableBtn",
  props: {
    imageFiles: Array,
    images: Array
  },
  data() {
    return {
      table: []
    };
  },
  methods: {
    async create() {
      if (this.imageFiles) {
        let audio = new Audio(sound);
audio.play();
        const formData = new FormData();

        for (let i = 0; i < this.imageFiles.length; i++) {
          formData.append("files", this.imageFiles[i]);
        }

        try {
          const response = await axios.post(
            "http://localhost:8000/multiple_files",
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );

          for (let i = 0; i < response.data.length; i++) {
            try {
              const plantDiseaseObj = await axios.get(
                "http://localhost:8000/plant_disease/" +
                  response.data[i].Result
              );
        //       var reader = new FileReader();
        //       var imageUrl;
        // reader.onload = function (event) {
        //   imageUrl = event.target.result;
          
        // };

              this.table.push({
                "Ảnh": this.images[i].image,
                "Tên file": response.data[i].Sample,
                "Loại cây": plantDiseaseObj.data.plant,
                "Tình trạng": plantDiseaseObj.data.disease,
                "Class": plantDiseaseObj.data.name,
                "Độ tin cậy": response.data[i].Confidence
              })


            } catch (error) {
              console.error(error);
            }
          }


          this.$emit("table", this.table);
          this.$emit("createClick", true);
            this.$emit("reset", false);
        } catch (error) {
          console.error(error);
        }
      }
    },
  },
};
</script>

<style>

.create-btn {

  display: block;
  margin-left: auto;
  margin-right: auto;
  background-color: #3a9e5b;
  height: 50px;
  width: 200px;
  border-radius: 50px;
  color: white;
  font-family: 'AR One Sans';
  font-size: 24px;
}

.create-btn:hover {
  background-color: #286f40;
}
</style>
