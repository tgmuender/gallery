import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here

import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { ImageDetailComponent } from './image-detail/image-detail.component';
import { ImageListService } from "./image-list.service";
import { HttpClientModule } from '@angular/common/http';
import {ImageDetailService} from "./image-detail.service";


@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    ImageDetailComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    ImageListService,
    ImageDetailService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
