import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatTabsModule} from "@angular/material/tabs";
import { HeaderComponent } from './Components/header/header.component';
import { DataRegisterComponent } from './Components/data-register/data-register.component';
import { SystemsEngineerComponent } from './Components/systems-engineer/systems-engineer.component';
import {MatTableModule} from "@angular/material/table";
import { DownloadButtonComponent } from './Components/download-button/download-button.component';
import {MatIconModule} from "@angular/material/icon";
import { SubjectListComponent } from './Components/subject-list/subject-list.component';
import {MatChipsModule} from "@angular/material/chips";
import { ElectronicEngineerComponent } from './Components/electronic-engineer/electronic-engineer.component';
import { TeachersComponent } from './Components/teachers/teachers.component';
import { OthersComponent } from './Components/others/others.component';
import { TableContentComponent } from './Components/table-content/table-content.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    DataRegisterComponent,
    SystemsEngineerComponent,
    DownloadButtonComponent,
    SubjectListComponent,
    ElectronicEngineerComponent,
    TeachersComponent,
    OthersComponent,
    TableContentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTabsModule,
    MatTableModule,
    MatIconModule,
    MatChipsModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
