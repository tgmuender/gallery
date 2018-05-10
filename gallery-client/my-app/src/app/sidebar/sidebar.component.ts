import { Component, OnInit } from '@angular/core';
import { PreviewImage} from "../PreviewImage";
import { ImageListService} from "../image-list.service";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {

  previewImages: PreviewImage[];

  previewImage: PreviewImage;

  onSelect(previewImage: PreviewImage): void {
    this.previewImage = previewImage;
  }

  getPreviewImages(): void {
    this.imageListService.getImages()
      .subscribe(images => this.previewImages = images);
  }

  constructor(private imageListService: ImageListService) { }

  ngOnInit() {
    this.getPreviewImages();
  }

}
