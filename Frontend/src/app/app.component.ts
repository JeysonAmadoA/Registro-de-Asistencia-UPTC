import { Component, OnInit } from '@angular/core';
import { IndexService } from './Services/index.service';
import { take } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  /**
   *
   */
  constructor(private indexService : IndexService) {
    
  }

  title = 'Registro Asistencia';

  ngOnInit(): void {
    this.indexService.registerData()
      .pipe(
        take(1) 
      )
      .subscribe((res: any) => {
        console.log(res);
      });
  }
}
