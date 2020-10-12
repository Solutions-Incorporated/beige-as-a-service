<script lang="ts">
  let files: string[] | Blob[];
  let statusCode = "";
 
  async function handleSubmit() {
    if (files.length > 0) {
      const formData = new FormData();
      formData.append("file", files[0]);
      console.log(formData)
      const response = await fetch("http://0.0.0.0:8000/color/what", {
        method: "POST",
        body: formData
      });

      console.log(response);

      statusCode = response.status;
    }
  }
</script>
 
{statusCode}

<form on:submit|preventDefault={handleSubmit}>
  <label for="file">File</label>
  <input required id="file" type="file" bind:files />
  <input type="submit" value="Upload file" />
</form>