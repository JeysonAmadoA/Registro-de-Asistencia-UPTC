import { Component, OnInit } from '@angular/core';
import { IndexService } from 'src/app/Services/index.service';


@Component({
  selector: 'app-systems-engineer',
  templateUrl: './systems-engineer.component.html',
  styleUrls: ['./systems-engineer.component.scss']
})

export class SystemsEngineerComponent implements OnInit {
  
  indexData = [];
  dataSource = [];
  columns: string[] = [];
  subjects: string[] = [];
  subjectFilter:string = ''
  downloadFile:string = 'http://localhost:5000/file/generar_archivo_sistemas' 

  constructor(private indexService: IndexService ) {}

  ngOnInit(): void {

    setTimeout(() => {
      this.indexService.getSystemEngineerData()
          .subscribe((res: any) => {
            const firstObject = res[0];
            const dateKeys = Object.keys(firstObject).filter(key => key !== 'Nombre' && key !== 'Correo' && key !== 'Programa' && key !== 'Asignatura');
            this.columns = ['Nombre', 'Correo', 'Programa', 'Asignatura', ...dateKeys];
            this.indexData = res
            this.dataSource = this.indexData;

            const filteredObjects = res.filter((obj:any) => obj.Asignatura !== null && obj.Asignatura !== undefined);
            const asignaturasSet = new Set<string>(filteredObjects.map((obj:any) => obj.Asignatura));
            const asignaturasArray = Array.from(asignaturasSet);
            this.subjects = asignaturasArray;
          });
    }, 5000);
    
  }

  filterData(subjectFilter:string){
    if(this.subjectFilter===subjectFilter){
      this.dataSource = this.indexData;
      this.subjectFilter = '';
    }
    else{
      let filteredData = this.indexData.filter((obj:any) => obj.Asignatura === subjectFilter);
      this.dataSource = filteredData;
      this.subjectFilter = subjectFilter;
    }
  }
}
