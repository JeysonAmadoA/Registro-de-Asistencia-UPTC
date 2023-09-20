import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-table-content',
  templateUrl: './table-content.component.html',
  styleUrls: ['./table-content.component.scss']
})
export class TableContentComponent {
  headerColor : string = '#4b832b'
  @Input() displayedColumns: string[] = [];
  @Input() data: any[] = [];
  @Input() dateIndex: number = 0;
}
