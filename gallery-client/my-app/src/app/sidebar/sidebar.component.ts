import { Component, OnInit } from '@angular/core';
import { PreviewImage} from "../PreviewImage";
import { PREVIEW_IMAGES} from "../mock-preview-images";


@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {

  previewImages = PREVIEW_IMAGES;

  previewImage: PreviewImage;

  onSelect(previewImage: PreviewImage): void {
    this.previewImage = previewImage;
  }

  constructor() { }

  ngOnInit() {
  }

}
