<template>
  <button @click="exportDataToCSV" class="export-btn">Xuất file CSV</button>
</template>

<script>
const sound = require('../assets/download.mp3');

export default {
  name: "ExportCSVBtn",
  data() {
    return {
      csvTable: []
    };
  },  
  props: {
    csv: Array
  },
  methods: {
    // matchResults(fileName, className) {
    //   if ((fileName.includes("C__H_") && className.includes("Coffee__H"))
    //   ||  (fileName.includes("C__M_") && className.includes("Coffee__M"))
    //   ||  (fileName.includes("C__P_") && className.includes("Coffee__P"))
    //   ||  (fileName.includes("C__R_") && className.includes("Coffee__R"))
    //   ||  (fileName.includes("CM__CLS_") && className.includes("Corn_(Maize)__Ce"))
    //   ||  (fileName.includes("CM__CR_") && className.includes("Corn_(Maize)__Co"))
    //   ||  (fileName.includes("CM__H_") && className.includes("Corn_(Maize)__H"))
    //   ||  (fileName.includes("CM__NLB_") && className.includes("Corn_(Maize)__N"))
    //   ||  (fileName.includes("G__B_") && className.includes("Grape__B"))
    //   ||  (fileName.includes("G__E_") && className.includes("Grape__E"))
    //   ||  (fileName.includes("G__H_") && className.includes("Grape__H"))
    //   ||  (fileName.includes("G__L_") && className.includes("Grape__L"))
    //   ||  (fileName.includes("J__A_") && className.includes("Jackfruit__A"))
    //   ||  (fileName.includes("J__B_") && className.includes("Jackfruit__B"))
    //   ||  (fileName.includes("J__H_") && className.includes("Jackfruit__H"))
    //   ||  (fileName.includes("M__A_") && className.includes("Mango__A"))
    //   ||  (fileName.includes("M__B_") && className.includes("Mango__B"))
    //   ||  (fileName.includes("M__C_") && className.includes("Mango__C"))
    //   ||  (fileName.includes("M__D_") && className.includes("Mango__D"))
    //   ||  (fileName.includes("M__G_") && className.includes("Mango__G"))
    //   ||  (fileName.includes("M__H_") && className.includes("Mango__H"))
    //   ||  (fileName.includes("M__P_") && className.includes("Mango__P"))
    //   ||  (fileName.includes("M__S_") && className.includes("Mango__S"))
    //   ||  (fileName.includes("R__BLB_") && className.includes("Rice__Ba"))
    //   ||  (fileName.includes("R__BS_") && className.includes("Rice__Br"))
    //   ||  (fileName.includes("R__H_") && className.includes("Rice__H"))
    //   ||  (fileName.includes("R__LB_") && className.includes("Rice__Leaf_B"))
    //   ||  (fileName.includes("R__LS_") && className.includes("Rice__Leaf_S"))
    //   ||  (fileName.includes("R__NBS_") && className.includes("Rice__N"))
    //   ||  (fileName.includes("S__H_") && className.includes("Sugarcane__H"))
    //   ||  (fileName.includes("S__M_") && className.includes("Sugarcane__M"))
    //   ||  (fileName.includes("S__RR_") && className.includes("Sugarcane__Re"))
    //   ||  (fileName.includes("S__R_") && className.includes("Sugarcane__Ru"))
    //   ||  (fileName.includes("S__Y_") && className.includes("Sugarcane__Y"))
    //   ||  (fileName.includes("T__A_") && className.includes("Tea__A"))
    //   ||  (fileName.includes("T__B_") && className.includes("Tea__B"))
    //   ||  (fileName.includes("T__G_") && className.includes("Tea__G"))
    //   ||  (fileName.includes("T__H_") && className.includes("Tea__Hea"))
    //   ||  (fileName.includes("T__HS_") && className.includes("Tea__Hel"))
    //   ||  (fileName.includes("T__R_") && className.includes("Tea__R"))

    //  ) {
    //   return "Đúng";
    //  }
    //  else {
    //   return "Sai";

    
    //  }
    // },


    exportDataToCSV() {
      let audio = new Audio(sound);
audio.play();
      for (let i = 0; i < this.csv.length; i++) {
        if (this.csv[i]["Độ tin cậy"] >= 0.7) {
        this.csvTable.push(
          {
            "Ảnh": this.csv[i]["Tên file"],
            "Loại cây": this.csv[i]["Loại cây"],
            "Tình trạng": this.csv[i]["Tình trạng"],
            // "Độ tin cậy": (this.csv[i]["Độ tin cậy"] * 100).toFixed(2) + '%'
            // "Kết quả": this.matchResults(this.csv[i]["Tên file"], this.csv[i]["Class"])
          }
        );
        }
        else {
          this.csvTable.push(
          {
            "Ảnh": this.csv[i]["Tên file"],
            "Loại cây": "Không xác định",
            "Tình trạng": "-",
            // "Độ tin cậy": "-"
            // "Kết quả": this.matchResults(this.csv[i]["Tên file"], this.csv[i]["Class"])
          }
        );          
        }
      }
      // const csvData = this.csvTable;
      // const total = this.csvTable.length;
      // const nUndefined = this.csvTable.filter(function(item){ return item['Loại cây'] == "Không xác định";}).length;
      // const nSuccess = total - nUndefined
      // // const nTrue = this.csvTable.filter(function(item){ return item['Kết quả'] == "Đúng";}).length;
      // // const nFalse = this.csvTable.filter(function(item){ return item['Kết quả'] == "Sai";}).length;
      // const nTrue = this.csvTable.filter(function(item){ return item['Kết quả'] == "Đúng" && item['Loại cây'] != "Không xác định";}).length;
      // const nFalse = this.csvTable.filter(function(item){ return item['Kết quả'] == "Sai" && item['Loại cây'] != "Không xác định";}).length;

      // this.csvTable.push({
      //   "Ảnh": "Số ảnh dự đoán được",
      //       "Loại cây": nSuccess,
      //       "Tình trạng": "Tỉ lệ",
      //       "Độ tin cậy": ((nSuccess / total) * 100).toFixed(2) + '%'
      // })
      // this.csvTable.push({
      //   "Ảnh": "Số ảnh không xác định",
      //       "Loại cây": nUndefined,
      //       "Tình trạng": "Tỉ lệ",
      //       "Độ tin cậy": ((nUndefined / total) * 100).toFixed(2) + '%'
      // })
      // this.csvTable.push({
      //   "Ảnh": "Tổng cộng",
      //       "Loại cây": total,
      //       "Tình trạng": "Tỉ lệ",
      //       "Độ tin cậy": ((total / total) * 100).toFixed(2) + '%'
      // })
      // this.csvTable.push({
      //   "Ảnh": "Số dự đoán đúng",
      //       "Loại cây": nTrue,
      //       "Tình trạng": "Tỉ lệ",
      //       "Độ tin cậy": ((nTrue / nSuccess) * 100).toFixed(2) + '%'
      //       // "Độ tin cậy": ((nTrue / total) * 100).toFixed(2) + '%'

      // })
      // this.csvTable.push({
      //   "Ảnh": "Số dự đoán sai",
      //       "Loại cây": nFalse,
      //       "Tình trạng": "Tỉ lệ",
      //       "Độ tin cậy": ((nFalse / nSuccess) * 100).toFixed(2) + '%'
      //       // "Độ tin cậy": ((nFalse / total) * 100).toFixed(2) + '%'

      // })
      console.log('csv export: ', this.csvTable);
      const data = this.csvTable;
      const csvContent = this.convertToCSV(data);
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'results.csv');
      link.click();

    },
    convertToCSV(data) {
      const headers = Object.keys(data[0]);
      const rows = data.map(obj => headers.map(header => obj[header]));
      const headerRow = headers.join(',');
      const csvRows = [headerRow, ...rows.map(row => row.join(','))];
      return csvRows.join('\n');
    }
  },
};
</script>

<style>
.export-btn {
  display: block;
  background-color: #39483e;
  color: white;
  cursor: pointer;
  padding: 5px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  font-family: 'AR One Sans';


  height: 50px;
  width: 200px;
  border-radius: 50px;
  font-size: 24px;
}

.export-btn:hover {
  background-color: black;
}
</style>
