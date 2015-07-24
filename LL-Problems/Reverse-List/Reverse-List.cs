using System;
using System.Linq;
using System.Collections.Generic;

public class ReverseListSolution
{
    /// <summary>
    /// A simple Node class.
    /// </summary>
    /// <typeparam name="T">The type of Data.</typeparam>
    public class Node<T>
    {
        public T Data { get; set; }
        public Node<T> Next { get; set; }

        public Node(T data, Node<T> next = null)
        {
            Data = data;
            Next = next;
        }

        public static Node<T> SeqToLL(IEnumerable<T> seq)
        {
            Node<T> head = null;
            foreach (var value in seq.Reverse())
            {
                head = new Node<T>(value, head);
            }
            return head;
        }

        public override string ToString()
        {
            List<T> values = new List<T>();
            for (var p = this; p != null; p = p.Next)
            {
                values.Add(p.Data);
            }
            return "[" + string.Join(", ", values) + "]";
        }

        /// <summary>
        /// Reverses the given linked list in-place.
        /// </summary>
        /// <param name="head">The head of the linked list.</param>
        /// <returns>The new head of the reversed linked list.</returns>
        public static Node<T> ReverseList(Node<T> head)
        {
            Node<T> prev = null;
            var curr = head;
            while (curr != null)
            {
                var next = curr.Next;
                curr.Next = prev;
                prev = curr;
                curr = next;
            }
            return prev;
        }
    }

    /// <summary>
    /// The entry point.
    /// </summary>
    public static void Main()
    {
        var testHeads = new[]
        { 
            Node<int>.SeqToLL(new int[] {  }),
            Node<int>.SeqToLL(new int[] { 1 }),
            Node<int>.SeqToLL(new int[] { 1, 2 }),
            Node<int>.SeqToLL(new int[] { 1, 2, 3 }),
            Node<int>.SeqToLL(new int[] { 1, 2, 3, 4 })
        };
        for (var i = 0; i < testHeads.Length; i++)
        {
            Console.WriteLine("Test Case #{0}:", i + 1);
            Console.WriteLine(string.Format("    BEFORE: {0}", testHeads[i]));
            testHeads[i] = Node<int>.ReverseList(testHeads[i]);
            Console.WriteLine(string.Format("     AFTER: {0}", testHeads[i]));
        }
    }
}