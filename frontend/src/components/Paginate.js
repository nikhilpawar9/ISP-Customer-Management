import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";

const Paginate = ({
  customersperPage,
  customersCount,
  changePage,
  previousPage,
  nextPage,
}) => {
  const pageNumbers = [];

  const [maxPageCount, setMaxPageCount] = useState(5);
  const [minPageCount, setMinPageCount] = useState(0);

  for (let i = 1; i <= Math.ceil(customersCount / customersperPage); i++) {
    pageNumbers.push(i);
  }

  return (
    <div className="paginate mt-4">
      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center">
          <li className="page-item">
            <a onClick={() => previousPage()} href="#" className="page-link m-1">
              Prev
            </a>
          </li>
          {pageNumbers.map((number) => {
            if (number < maxPageCount + 1 && number > minPageCount) {
              return (
                <li className="page-item" key={number}>
                  <a
                    onClick={() => {
                      changePage(number);
                    }}
                    href="#"
                    className="page-link m-1"
                  >
                    {number}
                  </a>
                </li>
              );
            }
          })}
          <li className="page-item">
            <a onClick={() => nextPage()} href="#" className="page-link m-1">
              Next
            </a>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Paginate;
