import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class IndexService {

  constructor(private http:HttpClient) { }


  registerData(){
    return this.http.get('http://localhost:5000/process/register_data_default');
  }

  registerAssistance(){
    return this.http.get('http://localhost:5000/process/register_assistance');
  }

  getSystemEngineerData(){
    return this.http.get('http://localhost:5000/data/ingenieria_de_sistemas');
  }

  getElectronicEngineerData(){
    return this.http.get('http://localhost:5000/data/ingenieria_electronica');
  }

  getTeachersData(){
    return this.http.get('http://localhost:5000/data/docentes');
  }

  getOthersData(){
    return this.http.get('http://localhost:5000/data/otros');
  }
}
