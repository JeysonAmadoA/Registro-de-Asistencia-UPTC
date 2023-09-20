import { Component } from '@angular/core';

@Component({
  selector: 'app-data-register',
  templateUrl: './data-register.component.html',
  styleUrls: ['./data-register.component.scss']
})
export class DataRegisterComponent {
  fileName: string = 'Seleccione un archivo';

  updateFileName(fileInput: HTMLInputElement): void {
    if (fileInput.files && fileInput.files.length > 0) {
      this.fileName = fileInput.files[0].name;
    } else {
      this.fileName = 'Seleccione un archivo';
    }
  }
}

