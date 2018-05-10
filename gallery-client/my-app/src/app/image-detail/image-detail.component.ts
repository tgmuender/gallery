import {Component, OnInit, Input, OnChanges, SimpleChanges} from '@angular/core';
import { PreviewImage} from "../PreviewImage";
import { ImageDetails} from "../ImageDetails";
import {ImageDetailService} from "../image-detail.service";

@Component({
  selector: 'app-image-detail',
  templateUrl: './image-detail.component.html',
  styleUrls: ['./image-detail.component.css']
})
export class ImageDetailComponent implements OnInit, OnChanges {

  @Input() image: PreviewImage;

  details: ImageDetails;

  constructor(private imageDetailService: ImageDetailService) { }

  ngOnInit() {
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes.image && changes.image.currentValue) {
      var newImage = changes.image.currentValue['name'];
      console.log(newImage)

      this.imageDetailService.getImageDetails(newImage).subscribe(details => this.details = details);
    }
  }

}
